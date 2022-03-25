from unittest import result
from cv2 import mean
import pandas as pd
import statistics

df = pd.read_csv("data.csv")
height = df["Height(Inches)"].tolist()
mean = statistics.mean(height)
median = statistics.median(height)
mode = statistics.mode(height)
stdev = statistics.stdev(height)

print(mean)
print(median)
print(mode)
print(stdev)

sd1Start = mean - stdev
sd1end = mean + stdev

sd2start = mean - (2*stdev)
sd2end = mean + (2*stdev)

sd3start = mean - (3*stdev)
sd3end = mean + (3*stdev)

heightsd1 = [result for result in height if result > sd1Start and result < sd1end]
heightsd2 = [result for result in height if result > sd2start and result < sd2end]
heightsd3 = [result for result in height if result > sd3start and result < sd3end]

percentheightsd1 = (len(heightsd1)/len(height)) *100
percentheightsd2 = (len(heightsd2)/len(height)) *100
percentheightsd3 = (len(heightsd3)/len(height)) *100

print(percentheightsd1)
print(percentheightsd2)
print(percentheightsd3)