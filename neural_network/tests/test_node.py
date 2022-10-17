from node import *

node_0 = node()
node_1 = node()
node_2 = node()
node_3 = node()
node_4 = node()
node_5 = node()
node_6 = node()
node_7 = node()
node_8 = node()
node_9 = node()

node_0._init_()
node_1._init_()
node_2._init_()
node_3._init_()
node_4._init_()
node_5._init_()
node_6._init_()
node_7._init_()
node_8._init_()
node_9._init_()

node_0.value = 1
node_1.value = 1
node_2.value = 1
node_3.value = 1
node_4.value = 1
node_5.value = 1
node_6.value = 1
node_7.value = 1
node_8.value = 1

node_9.incoming = [(node_6, node_9, 1), (node_7, node_9, 1), (node_8, node_9, 1)]
node_6.incoming = [(node_5, node_6, 1), (node_4, node_6, 1), (node_3, node_6, 1)]
node_4.incoming = [(node_5, node_4, 1), (node_2, node_4, 1), (node_1, node_4, 1)]
node_1.incoming = [(node_0, node_1, 1)]

answer = node_9.get_value()

assert answer == 10
