#Setup
for (setup in 1:1) {
  setwd("C:/Users/Armin/Desktop/Data Science/Semantic Systems/")
  #Load libraries
  for (libs in 1:1) {

  }
}  

#Load data and preprocessing
#Countries
data.countries = read.csv("Countries.csv")
write.csv(data.countries, file = "data.countries.csv", row.names = FALSE)

#Population Vienna
data.pop.vienna = read.csv("bevoelkerung_tab_5.1.2.csv", sep = ";")[-c(1,27),c(1,18)]
names(data.pop.vienna) = c("Districtname", "Population")

Districts = as.character(data.pop.vienna$Districtname)[3:nrow(data.pop.vienna)]
Districts = strsplit(Districts, " ")
data.pop.vienna$District = NA
data.pop.vienna$Districtname = as.character(data.pop.vienna$Districtname)
for (i in 1:length(Districts)) {
  data.pop.vienna$District[i+2] = as.numeric(Districts[[i]][1])
  st = ifelse(i >= 10, 4, 3)
  data.pop.vienna$Districtname[i+2] = substr(data.pop.vienna$Districtname[i+2], st, nchar(data.pop.vienna$Districtname[i+2]))
}
write.csv(data.pop.vienna, file = "data.pop.vienna.csv", row.names = FALSE)

#Streets Vienna
data.streets.vienna = read.csv("strassen.csv")[,c(3,5,9)]
names(data.streets.vienna) = c("Streetname", "District", "Type")
write.csv(data.streets.vienna, file = "data.streets.vienna.csv", row.names = FALSE)
