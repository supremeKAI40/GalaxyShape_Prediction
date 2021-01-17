# GalaxyShape from RedShift Data
A machine learning model to learn and implement classification of galaxies from the telescopic data.
I have tried to implement algorithms, namely Decsion Tree and Random Forest Classifer to predict shape for the galaxies. 
I have used data from Sloan Digital Sky Survey, although there a GigaBytes of data, I have scavenged a smaller part of it, in the form of numpy array.
The given programs are just an attempt to get an experience with telescopic data.

From physics point-of-view, Red shift are the direct result of Doppler's effect, and is helpful to exactly know what is the distance of an object. 
The more the distance more is it shifted towards redder wavelngths of the spectrum, due to the fact that Universe is expanding farther from us.
It is also helpful for detection of size of object, for example if the size is very big, the light from near end will be less red shifted than the light from farther end.
SDSS data takes different measurements in 3 filters which is also available in the website.
And here, I have tried to interpret those data and human classified labels for those galaxies to form a dataset to help my model, predict shape of a  galaxy whether it is spiral or not, or if it's merging. 
