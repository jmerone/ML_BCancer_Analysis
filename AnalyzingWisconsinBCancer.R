
bcancer <- read.csv(
  "http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
         header = FALSE)
library(rpart)

colnames(bcancer) <- c(
'id_number',
'Clump_Thickness',
   'Uniformity_of_Cell_Size',
   'Uniformity_of_Cell_Shape',
   'Ma1rginal_Adhesion',
 'Single_Epithelial_Cell_Size',
 'Bare_Nuclei', 
'Bland_Chromatin',
'Normal_Nucleoli',
'Mitoses', 
'Class'
)

library(dplyr)

bcancer <- bcancer %>% 
  mutate(Class = ifelse(Class == 4, 1,0))

p <- rpart(Class ~ ., data = bcancer )
View(bcancer)
