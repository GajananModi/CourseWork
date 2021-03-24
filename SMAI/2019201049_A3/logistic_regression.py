import numpy as  np 
from PIL import Image
import sys
import os
opt = {
	'image_size': 32,
	'is_grayscale': True,
	'num_classes':0,
	'val_split': 0.7
}
# Load images
if len(sys.argv) < 3:
	sys.exit()

# Load Image using PIL for dataset
double_dict = {}
def load_image(path):
	im = Image.open(path).convert('L' if opt['is_grayscale'] else 'RGB')
	im = im.resize((opt['image_size'],opt['image_size']))
	im = np.array(im)
	im = im/256
	return im

# Load the full data from directory
def load_data(train_txt,test_txt):
	image_list = []
	y_list = []

	image_test = []

	with open(train_txt,'r') as f:
		for line in f.read().split('\n'):
			try:
				filename,y_name = line.split(' ')
				im = load_image(filename)
				image_list.append(im)
				if y_name in double_dict:
					y = double_dict[y_name]
				else:
					double_dict[y_name] = opt['num_classes']
					double_dict[opt['num_classes']] = y_name
					y = opt['num_classes']
					opt['num_classes'] += 1

				y_list.append(y)

			except Exception as e:
				pass

	image_list = np.array(image_list)
	y_list = np.array(y_list)

	with open(test_txt,'r') as f:
		for line in f.read().split('\n'):
			try:
				im = load_image(line)
				image_test.append(im)
			except:
					pass

	image_test = np.array(image_test)

	return image_list,y_list,image_list

# Load the data
X,y,X_test = load_data(sys.argv[1],sys.argv[2])
N,W,H = X.shape[0:3]
C = 1 if opt['is_grayscale'] else X.shape[3]

# Flatten to apply PCA
X = X.reshape((N,np.prod(X.shape[1:])))

def get_eigen_vectors(X):
	"""
		Get the eigen vectors of the covariance matrix
		also sort them by eigen value
	"""
	X_cov = np.cov(X.T)
	eig_val, eig_vec = np.linalg.eig(X_cov)
	sort_ind = np.argsort(eig_val)[::-1]
	eig_vec = eig_vec[sort_ind,:]
	return eig_vec

eig_vec = get_eigen_vectors(X)

def get_pca(X,eig_vec,k):
	"""
		Get PCA of K dimension using the top eigen vectors 
		by eigen value
		Also return the reconstructed data using just the top K vectors
	"""
	return np.real(X.dot(eig_vec[0:k,:].T)) , np.abs(X.dot(eig_vec[0:k,:].T.dot(eig_vec[0:k,:])))


# Get the PCA of K=32 to solve
K = 32
X = X.reshape((N,np.prod(X.shape[1:])))
X,_ = get_pca(X,eig_vec,K)

X_test = X_test.reshape((X_test.shape[0],np.prod(X_test.shape[1:])))
eig_vec_test = get_eigen_vectors(X_test)
X_test,_ = get_pca(X_test,eig_vec_test,K)

# Training and validation split
val_ind = int(opt['val_split']*X.shape[0])
X_val = X[val_ind:N]
X = X[0:val_ind]
y_val = y[val_ind:N]
y = y[0:val_ind]
N = val_ind

# Params
W = np.random.random((K,opt['num_classes']))
b = np.zeros(opt['num_classes'])
# Hyper Params
lr = 0.001
reg = 0.001
epochs = 3000
print_iter = 200
decay_iter = 1500
# Loss Variables
prev_loss = 0
loss_hist = []
acc_hist = []
val_acc_hist = []


y_gtr = np.zeros((N,opt['num_classes']))
y_gtr[np.arange(0,N), y] = 1
for epoch in range(epochs):
    
    # Forward prop
    y_pred = X.dot(W) + b
    softmax = np.exp(y_pred)/np.sum(np.exp(y_pred),axis=1)[:, np.newaxis]
    loss = -np.mean(np.log(softmax[np.arange(0,N), y])) + 0.5*reg*np.sum(W*W)

    loss_hist.append(loss)


    # Backprop
    dL = y_pred.copy()
    dL[np.arange(0,N), y] -= 1
    # dW for weights
    dW = X.T.dot(dL)
    W -= lr*dW
    W += reg*W

    if epoch % print_iter == 0:
        acc = np.sum(np.argmax(y_pred,axis=1) == y)/N
        val_y = X_val.dot(W) + b
        acc_val = np.sum(np.argmax(val_y,axis=1) == y_val)/520

        # print("Epoch:{} Loss:{} Acc:{} Validation Acc:{}".format(epoch,loss,acc,acc_val))
        
        acc_hist.append(acc)
        val_acc_hist.append(acc_val)
        if epoch > decay_iter:
            lr = lr//2
            reg = 4*reg//5
        
    prev_loss = loss


y_test = X_test.dot(W) + b
y_test = np.argmax(y_test,axis=1)
for y in y_test:
	print(double_dict[y])