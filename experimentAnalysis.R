#Final Project Q370 Data Analysis

library(dplyr) 
library(ggplot2) 
library(reshape2)

data<-read.table("main_data.txt", header = TRUE,sep=" ")

t.test(data$phone,data$nophone,paired=TRUE)

mean(data$phone)
mean(data$nophone)

long<-melt(data,measure.vars=c("phone","nophone"),id.vars="subject",variable.name="PhonePresense",value.name="Recall") #convert from wide to long format
ggplot(long,aes(x=PhonePresense,y=Recall,fill=PhonePresense))+stat_summary(fun=mean,geom="bar")+stat_summary(fun.data=mean_cl_normal,geom="errorbar")+ xlab("Availability of Phone") + ylab("Accuracy Score")
data$diff<-data$nophone-data$phone
cor.test(data$usage,data$diff)

plot(data$usage,data$diff)
abline(lm(data$diff ~ data$usage))

