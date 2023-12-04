library(tidyverse) 
library(dplyr)
library(stringr)
library(readr)


#read in the data
data <- read.table(file = here::here("2023/day1/day1_data.txt"), header = FALSE)


#### part 1 #########

#extract digits from string
 x <- data %>% 
         rowid_to_column() %>% 
         mutate(V2 = (str_extract_all(V1, "[0-9]"))) %>%
         group_by(rowid) 
 # mutate(total = paste0(first,last)  )

#better way for doin gthis im sure
i = 1
first <- list()
for(i in 1:length(x$V2)) {
head(unlist(x$V2[i]),n=1)
  x$first[i] <- head(unlist(x$V2[i]),n=1)
  x$last[i] <- tail(unlist(x$V2[i]),n=1)
}

#paste the numbers together and find the sum
x %>% 
  mutate(total = as.numeric(paste0(first,last))) %>% 
  ungroup() %>% 
  summarise(sum(total))



#### Part 2 #####  
string_to_digit <-
  data.frame(number = c("one","two","three",
                        "four","five","six",
                        "seven","eight","nine"),
             digit = c(1,2,3,4,5,6,7,8,9))

y <- data %>% 
  rowid_to_column() %>% 
  mutate(V2 = str_replace_all(V1, c("eight" = "8", "nine" = "9","five" = "5", "three" = "3",
                                    "six" = "6","one" = "1","seven" = "7",  "two" = "2",
                                    "four" = "4"
                                    ))) %>% 
  mutate(V3 = (str_extract_all(V2, "[0-9]"))) %>%
  group_by(rowid) 



i = 1
first <- list()
for(i in 1:length(y$V3)) {
  # head(unlist(x$V2[i]),n=1)
  y$first[i] <- head(unlist(y$V3[i]),n=1)
  y$last[i] <- tail(unlist(y$V3[i]),n=1)
}

#paste the numbers together and find the sum
 y %>% 
  mutate(total = as.numeric(paste0(first,last))) %>% 
   ungroup() %>% 
   summarise(sum(total))

 