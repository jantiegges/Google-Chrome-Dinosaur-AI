"""
DecisionMaker
    get Image Frame and resize it
        Image should be 16x4x4
    add image to image_array (consists of 4 images) and delete the oldest one
    give image_array to QTable --> get out highest value
    send action to Dinosaur(action) dependent on highest QValue --> get reward back
    compute the new q-value: new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        ### alpha = Learning_rate, gamma = Discount
    store image_array and neq q_value in batch_array
"""