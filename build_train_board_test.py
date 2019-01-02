print(f"train data: {len(train_x)} train X shape: {train_x.shape}")
print(f"validation data: {len(validation_x)} validation X shape: {validation_x.shape}")
print(f"test data: {len(test_x)} test X shape: {test_x.shape}")

model = Sequential()
model.add(LSTM(128, input_shape = (train_x.shape[1:]), return_sequences=True))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(LSTM(128, input_shape = (train_x.shape[1:]), return_sequences=True))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(LSTM(128, input_shape = (train_x.shape[1:]), return_sequences=False))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Dense(32, activation = 'relu'))
model.add(Dropout(0.2))

model.add(Dense(1, activation = 'relu'))

opt = tf.keras.optimizers.Adam(lr = 0.001, decay = 1e-6)


'''
Make choice btw tow diff loss function: mse & mean_absolute_percentage_error
'''
model.compile(loss = 'mse', optimizer = opt, metrics = ['accuracy'])
#model.compile(loss = 'mean_absolute_percentage_error', optimizer = opt, metrics = ['accuracy'])

tensorboard = TensorBoard(log_dir = f'logs/{NAME}')

filepath = 'LSTM_ElecOnly_1d_{epoch:02d}-{val_acc:.3f}'
checkpoint = ModelCheckpoint("LSTM_1JAN2019/{}.model".format(filepath, monitor='val_acc',
                                                                    verbose = 1,
                                                                    save_best_only = True,
                                                                    mode = 'max'))

history = model.fit(train_x, train_y, batch_size = BATCH_SIZE,
                                        epochs = EPOCH,
                                        validation_data = (validation_x, validation_y),
                                        callbacks = [tensorboard, checkpoint])

# start at 01:39
# python -m tensorboard.main --logdir = logs

pred = model.predict(test_x)
pred = list(itertools.chain(*pred))
#print(pred)
#re_pred = scaler.invers_transform(pred)
#print(re_pred)
#print(test_y)

result = pd.DataFrame({'y_true':test_y,'y_pred':pred})
