{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "from keras.models import Sequential\n",
    "from keras.layers import Dense,LSTM,Dropout"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              Datetime  AEP_MW\n",
      "0      12/31/2004 1:00   13478\n",
      "1      12/31/2004 2:00   12865\n",
      "2      12/31/2004 3:00   12577\n",
      "3      12/31/2004 4:00   12517\n",
      "4      12/31/2004 5:00   12670\n",
      "5      12/31/2004 6:00   13038\n",
      "6      12/31/2004 7:00   13692\n",
      "7      12/31/2004 8:00   14297\n",
      "8      12/31/2004 9:00   14719\n",
      "9     12/31/2004 10:00   14941\n",
      "10    12/31/2004 11:00   15184\n",
      "11    12/31/2004 12:00   15009\n",
      "12    12/31/2004 13:00   14808\n",
      "13    12/31/2004 14:00   14522\n",
      "14    12/31/2004 15:00   14349\n",
      "15    12/31/2004 16:00   14107\n",
      "16    12/31/2004 17:00   14410\n",
      "17    12/31/2004 18:00   15174\n",
      "18    12/31/2004 19:00   15261\n",
      "19    12/31/2004 20:00   14774\n",
      "20    12/31/2004 21:00   14363\n",
      "21    12/31/2004 22:00   14045\n",
      "22    12/31/2004 23:00   13478\n",
      "23       1/1/2005 0:00   12892\n",
      "24     12/30/2004 1:00   14097\n",
      "25     12/30/2004 2:00   13667\n",
      "26     12/30/2004 3:00   13451\n",
      "27     12/30/2004 4:00   13379\n",
      "28     12/30/2004 5:00   13506\n",
      "29     12/30/2004 6:00   14121\n",
      "...                ...     ...\n",
      "2005   10/9/2004 15:00   13579\n",
      "2006   10/9/2004 16:00   13551\n",
      "2007   10/9/2004 17:00   13509\n",
      "2008   10/9/2004 18:00   13498\n",
      "2009   10/9/2004 19:00   13557\n",
      "2010   10/9/2004 20:00   14122\n",
      "2011   10/9/2004 21:00   14094\n",
      "2012   10/9/2004 22:00   13600\n",
      "2013   10/9/2004 23:00   12956\n",
      "2014   10/10/2004 0:00   12096\n",
      "2015    10/8/2004 1:00   12468\n",
      "2016    10/8/2004 2:00   12046\n",
      "2017    10/8/2004 3:00   11749\n",
      "2018    10/8/2004 4:00   11784\n",
      "2019    10/8/2004 5:00   11919\n",
      "2020    10/8/2004 6:00   12610\n",
      "2021    10/8/2004 7:00   14209\n",
      "2022    10/8/2004 8:00   15239\n",
      "2023    10/8/2004 9:00   15297\n",
      "2024   10/8/2004 10:00   15429\n",
      "2025   10/8/2004 11:00   15545\n",
      "2026   10/8/2004 12:00   15586\n",
      "2027   10/8/2004 13:00   15626\n",
      "2028   10/8/2004 14:00   15703\n",
      "2029   10/8/2004 15:00   15651\n",
      "2030   10/8/2004 16:00   15514\n",
      "2031   10/8/2004 17:00   15369\n",
      "2032   10/8/2004 18:00   15116\n",
      "2033   10/8/2004 19:00   14930\n",
      "2034   10/8/2004 20:00   15315\n",
      "\n",
      "[2035 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "dataset_train = pd.read_csv('PowerAep2.csv')\n",
    "training_set = dataset_train.iloc[:,1:2].values\n",
    "print(dataset_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sc = MinMaxScaler(feature_range = (0,1))\n",
    "training_set_scaled = sc.fit_transform(training_set)\n",
    "print(training_set_scaled[1974])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.26108494 0.21130421 0.18791619 0.18304369 0.19546857 0.22535326\n",
      " 0.27846354 0.32759461 0.36186454 0.3798928  0.39962644 0.38541497\n",
      " 0.36909209 0.34586649 0.33181744 0.31216502 0.33677115 0.39881436\n",
      " 0.40587949 0.36633101 0.33295436 0.3071301  0.26108494 0.21349683\n",
      " 0.31135293 0.27643333 0.25889232 0.25304531 0.26335878 0.31330193\n",
      " 0.39004385 0.44729576 0.46970927 0.48578853 0.49650804 0.47709924\n",
      " 0.45663472 0.42553191 0.40141303 0.38866331 0.39775865 0.47279519\n",
      " 0.50714634 0.49074224 0.48400195 0.4602891  0.40149423 0.32913757\n",
      " 0.40279357 0.36283904 0.34432353 0.33855774 0.34659737 0.39174923\n",
      " 0.46735423 0.54450219 0.55920091 0.56829625 0.56285529 0.54799415]\n",
      "60\n"
     ]
    }
   ],
   "source": [
    "x_train = []\n",
    "y_train = []\n",
    "for i in range(60,2035):\n",
    "    x_train.append(training_set_scaled[i-60:i, 0])\n",
    "    #y_train.append(training_set_scaled[i,0])\n",
    "    y_train.append(training_set_scaled[i,0])\n",
    "x_train, y_train = np.array(x_train), np.array(y_train)\n",
    "print(x_train[0])\n",
    "#print(x_train[1])\n",
    "#print(y_train[0])\n",
    "x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))\n",
    "#print(x_train)\n",
    "print(x_train.shape[1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/350\n",
      "1975/1975 [==============================] - 59s 30ms/step - loss: 0.0349\n",
      "Epoch 2/350\n",
      "1975/1975 [==============================] - 33s 17ms/step - loss: 0.0222\n",
      "Epoch 3/350\n",
      "1975/1975 [==============================] - 34s 17ms/step - loss: 0.0209\n",
      "Epoch 4/350\n",
      "1975/1975 [==============================] - 33s 17ms/step - loss: 0.0185\n",
      "Epoch 5/350\n",
      "1975/1975 [==============================] - 32s 16ms/step - loss: 0.0158\n",
      "Epoch 6/350\n",
      "1975/1975 [==============================] - 33s 17ms/step - loss: 0.0134\n",
      "Epoch 7/350\n",
      "1975/1975 [==============================] - 33s 17ms/step - loss: 0.0133\n",
      "Epoch 8/350\n",
      "1975/1975 [==============================] - 32s 16ms/step - loss: 0.0129\n",
      "Epoch 9/350\n",
      "1975/1975 [==============================] - 32s 16ms/step - loss: 0.0113\n",
      "Epoch 10/350\n",
      "1975/1975 [==============================] - 31s 16ms/step - loss: 0.0111\n",
      "Epoch 11/350\n",
      "1975/1975 [==============================] - 32s 16ms/step - loss: 0.0102\n",
      "Epoch 12/350\n",
      "1975/1975 [==============================] - 33s 17ms/step - loss: 0.0109\n",
      "Epoch 13/350\n",
      "1975/1975 [==============================] - 32s 16ms/step - loss: 0.0103\n",
      "Epoch 14/350\n",
      "1975/1975 [==============================] - 33s 17ms/step - loss: 0.0097\n",
      "Epoch 15/350\n",
      "1975/1975 [==============================] - 33s 16ms/step - loss: 0.0088\n",
      "Epoch 16/350\n",
      "1975/1975 [==============================] - 33s 16ms/step - loss: 0.0093\n",
      "Epoch 17/350\n",
      "1975/1975 [==============================] - 34s 17ms/step - loss: 0.0085\n",
      "Epoch 18/350\n",
      "1975/1975 [==============================] - 33s 17ms/step - loss: 0.0076\n",
      "Epoch 19/350\n",
      "1975/1975 [==============================] - 33s 17ms/step - loss: 0.0080\n",
      "Epoch 20/350\n",
      "1975/1975 [==============================] - 33s 17ms/step - loss: 0.0075\n",
      "Epoch 21/350\n",
      "1975/1975 [==============================] - 33s 17ms/step - loss: 0.0073\n",
      "Epoch 22/350\n",
      "1376/1975 [===================>..........] - ETA: 9s - loss: 0.0061 "
     ]
    }
   ],
   "source": [
    "model = Sequential()\n",
    "model.add(LSTM(units = 128, return_sequences=True,input_shape = (x_train.shape[1],1)))\n",
    "model.add(Dropout(0.2))\n",
    "model.add(LSTM(units = 64, return_sequences=True))\n",
    "model.add(Dropout(0.2))\n",
    "model.add(LSTM(units = 32, return_sequences=True))\n",
    "model.add(Dropout(0.2))\n",
    "model.add(LSTM(units = 32))\n",
    "model.add(Dropout(0.2))\n",
    "model.add(Dense(units = 1))\n",
    "model.compile(optimizer = 'adam', loss = 'mean_squared_error')\n",
    "model.fit(x_train,y_train,epochs = 350,batch_size = 32)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              Datetime  AEP_MW\n",
      "0      12/31/2004 1:00   13478\n",
      "1      12/31/2004 2:00   12865\n",
      "2      12/31/2004 3:00   12577\n",
      "3      12/31/2004 4:00   12517\n",
      "4      12/31/2004 5:00   12670\n",
      "5      12/31/2004 6:00   13038\n",
      "6      12/31/2004 7:00   13692\n",
      "7      12/31/2004 8:00   14297\n",
      "8      12/31/2004 9:00   14719\n",
      "9     12/31/2004 10:00   14941\n",
      "10    12/31/2004 11:00   15184\n",
      "11    12/31/2004 12:00   15009\n",
      "12    12/31/2004 13:00   14808\n",
      "13    12/31/2004 14:00   14522\n",
      "14    12/31/2004 15:00   14349\n",
      "15    12/31/2004 16:00   14107\n",
      "16    12/31/2004 17:00   14410\n",
      "17    12/31/2004 18:00   15174\n",
      "18    12/31/2004 19:00   15261\n",
      "19    12/31/2004 20:00   14774\n",
      "20    12/31/2004 21:00   14363\n",
      "21    12/31/2004 22:00   14045\n",
      "22    12/31/2004 23:00   13478\n",
      "23       1/1/2005 0:00   12892\n",
      "24     12/30/2004 1:00   14097\n",
      "25     12/30/2004 2:00   13667\n",
      "26     12/30/2004 3:00   13451\n",
      "27     12/30/2004 4:00   13379\n",
      "28     12/30/2004 5:00   13506\n",
      "29     12/30/2004 6:00   14121\n",
      "...                ...     ...\n",
      "2005   10/9/2004 15:00   13579\n",
      "2006   10/9/2004 16:00   13551\n",
      "2007   10/9/2004 17:00   13509\n",
      "2008   10/9/2004 18:00   13498\n",
      "2009   10/9/2004 19:00   13557\n",
      "2010   10/9/2004 20:00   14122\n",
      "2011   10/9/2004 21:00   14094\n",
      "2012   10/9/2004 22:00   13600\n",
      "2013   10/9/2004 23:00   12956\n",
      "2014   10/10/2004 0:00   12096\n",
      "2015    10/8/2004 1:00   12468\n",
      "2016    10/8/2004 2:00   12046\n",
      "2017    10/8/2004 3:00   11749\n",
      "2018    10/8/2004 4:00   11784\n",
      "2019    10/8/2004 5:00   11919\n",
      "2020    10/8/2004 6:00   12610\n",
      "2021    10/8/2004 7:00   14209\n",
      "2022    10/8/2004 8:00   15239\n",
      "2023    10/8/2004 9:00   15297\n",
      "2024   10/8/2004 10:00   15429\n",
      "2025   10/8/2004 11:00   15545\n",
      "2026   10/8/2004 12:00   15586\n",
      "2027   10/8/2004 13:00   15626\n",
      "2028   10/8/2004 14:00   15703\n",
      "2029   10/8/2004 15:00   15651\n",
      "2030   10/8/2004 16:00   15514\n",
      "2031   10/8/2004 17:00   15369\n",
      "2032   10/8/2004 18:00   15116\n",
      "2033   10/8/2004 19:00   14930\n",
      "2034   10/8/2004 20:00   15315\n",
      "\n",
      "[2035 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "dataset_test = pd.read_csv('PowerTest.csv')\n",
    "print(dataset_train)\n",
    "actual_power = dataset_test.iloc[:,1:2].values\n",
    "dataset_total = pd.concat((dataset_train['AEP_MW'],dataset_test['AEP_MW']),axis = 0)\n",
    "#print(dataset_total)\n",
    "inputs = dataset_total[len(dataset_total)-len(dataset_test)-60:].values\n",
    "inputs = inputs.reshape(-1,1)\n",
    "inputs = sc.transform(inputs)\n",
    "#print(inputs)\n",
    "x_test = []\n",
    "for i in range (60,76):\n",
    "    x_test.append(inputs[i-60:i,0])\n",
    "x_test = np.array(x_test)\n",
    "x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))\n",
    "#print(x_test)\n",
    "predicted_power = model.predict(x_test)\n",
    "pedicted_power = sc.inverse_transform(predicted_power)\n",
    "#print(predicted_stock)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x1af26a42320>]"
      ]
     },
     "execution_count": 201,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(actual_power, color = 'black', label = 'Actual')\n",
    "plt.plot(pedicted_power, color = 'green', label = 'Predicted')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
