import tensorflow as tf
import numpy as np

'''a=(tf.placeholder(tf.float32,[None]),tf.placeholder(tf.float32,[None]))
out=a[0]+a[1]

inp=(np.ones(2),np.ones(2))
sess=tf.InteractiveSession()
print(sess.run(out,feed_dict={a:inp}))'''
a=np.ones([1,10])
a[0,:4]=2
print(a)
