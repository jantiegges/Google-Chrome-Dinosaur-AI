"""
TrainBatch(batch_array)

"""

SAMPLES = 1000
GAMMA = 0.8
ALPHA = LR = 0.7
EPSILON_I = 0.1
EPSILON_F = 0.0001
DECAY_TIME = 800                 # Number of generation epsilon will take to reach epsilon_f
DECAY_STEP = (EPSILON_I-EPSILON_F)/DECAY_TIME

IMAGE_COL = 16
IMAGE_ROW = 4
IMAGE_FLOW = 4


import numpy as np
import Dinosaur
import DecisionMaker


def trainBatch(model, samples, labels):
    """
    Train the model on the training data samples with the result labels
    :return: None
    """
    epochs = 50        # epochs and bathcSize can be defined later
    batchSize = 50      # they should be defined to optimize learning speed
    model.fit(np.array(samples), np.array(labels),  epochs=epochs, batch_size=batchSize)


def updateImageFlow(imageFlow, current_arr):
    """
    Updates the array imageFlow
    :parameter: current imageFlow, new image
    :return: new imageFlow
    """
    imageFlow[3] = imageFlow[2]
    imageFlow[2] = imageFlow[1]
    imageFlow[1] = imageFlow[0]
    imageFlow[0] = current_arr
    return imageFlow


def propagateReward(resultArray, decisionTaken, reward, step):
    """
    Propagate the rewards to the old decision for the current run
    :parameter: Array containing the rewards, decision taken for each step, current reward, number of step of this run
    :return: new resultArray
    """
    i = 0
    m = len(resultArray)-1
    for i in range(1, step):
        resultArray[int(m-i)][int(decisionTaken[int(m-i)])] += LR * GAMMA**i * reward
    return resultArray




def trainModel(model, generation):
    """
    Script that runs the game and train the model
    :parameter: the model we use, generation = number of time the model trained a batch, if new model generation = 0
    :return: None
    """

    epsilon = EPSILON_I-generation*DECAY_STEP
    if epsilon < EPSILON_F:
        epsilon = EPSILON_F

    while True:

        generation += 1
        s = 0  # number of samples
        imageFlow = np.full((IMAGE_FLOW, IMAGE_ROW, IMAGE_COL), 247)  # array of 4 images used to take decision (position 0 most recent image)
        decision = np.zeros((1,2))  # array holding the result of the decision
        action = 0  # action taken by the dinosaur
        decisionTaken = np.zeros(1)  # decision Taken at each step
        stateArray = np.zeros((1, IMAGE_FLOW, IMAGE_ROW, IMAGE_COL))  # Array storing the image state by state
        resultArray = np.zeros((1, 2))  # Array storing the decision state by state


        while s < SAMPLES:
            step = 0  # Number of steps before dying
            alive = True  # state of the dinosaur
            reward = 0
            current_arr = DecisionMaker.getImage()              # startup : check if alive (should not be) and restart
            alive = Dinosaur.checkState(current_arr)
            if alive == False:
                Dinosaur.restart()
                alive = True
            current_arr = DecisionMaker.getImage()              # gets fist image after restarting

            while alive == True:
                step += 1
                imageFlow = updateImageFlow(imageFlow, current_arr)

                decision = DecisionMaker.takeDecision(model, np.array([imageFlow]))

                if np.random.random() <= epsilon:           # random chance of taking a random action
                    action = np.random.randint(0,2)
                else:
                    action = np.argmax(decision[0])         # 0 = keep running, 1 = jump, 2 = duck

                if step == 1:
                    decisionTaken[0] = action               # stores all the action taken to propagate the reward later
                else:
                    decisionTaken = np.append(decisionTaken, [action], axis=0)

                if action == 0:                             # gives reward and takes action
                    reward = 10
                elif action == 1:
                    Dinosaur.jump()
                    reward = 2

                current_arr = DecisionMaker.getImage()          # get new image
                alive = Dinosaur.checkState(current_arr)        # check if still alive

                if alive == False:
                    reward = -100

                decision[0][action] += LR*reward                # gives current reward

                if step == 1:
                    resultArray[0] = decision[0]                # stores the current decision table updated (Q-table)
                else:
                    resultArray = np.append(resultArray, decision, axis=0)
                                                                                            # propagate the current
                resultArray = propagateReward(resultArray, decisionTaken, reward, step)     # reward to previous
                                                                                            # decisions
                if step == 1:
                    stateArray[0] = imageFlow                                   # stores the current situation
                else:
                    stateArray = np.append(stateArray, [imageFlow], axis=0)

                if action == 1:                                                 # stops the action
                    Dinosaur.unJump()

                s += 1

        if epsilon >= EPSILON_F:                                        # decrease epsilon
            epsilon -= DECAY_STEP

        trainBatch(model, stateArray, resultArray)                      # train the model when enough data avaliable

        print("generation %d model trained" % generation)

        if generation%10 == 0:                                           # saves one model every 5 generations
            model.save("model_generation_%d.h5" % generation)

        Dinosaur.resetWebPage()

