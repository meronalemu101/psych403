face_list = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png']
house_list = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png']
cue_list = ['cue1', 'cue2']
facehouse = list(zip(face_list, house_list))
np.random.shuffle(facehouse)

print(list(zip(facehouse, cue_list)))
#I'm wanting to complete this to get the 100 trials for the scripts.
#Yet again i'm having issues with installing numpy on PyCharm.
#Need to see office hours to sort this.
