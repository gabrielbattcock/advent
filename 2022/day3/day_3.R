#day 3 of advent for code

#get wd and read in data
setwd("Documents/programming_projects/advent")
rucksack <- read.table("rucksack.txt")


string_split <- function(string){
  len <- nchar(string)
  split <- substring(string, seq(1, len, len/2), seq(len/2, len, len/2))
  split1 <- unlist(strsplit(split[1],""))
  split2 <- unlist(strsplit(split[2],""))
  common <- intersect(split1,split2)
  common
}

rucksack$letters <- lapply(rucksack$V1, string_split)
rucksack$number <- match(rucksack$letters, c(letters,LETTERS))
sum(rucksack$number)


#part 2
rucksack2 <- read.table("rucksack.txt")

#split groups of three into separate vectors

first <- rucksack2[seq(1, nrow(rucksack2), 3), ]
second <- rucksack2[seq(2, nrow(rucksack2), 3), ]
third <- rucksack2[seq(3, nrow(rucksack2), 3), ]

split2 <- function(x, y, z){
  x <- unlist(strsplit(x,""))
  y <- unlist(strsplit(y,""))
  z <- unlist(strsplit(z,""))
  common_letter <- Reduce(intersect, list(x, y, z))
  common_letter
}

#iterate over the vectors to find the common character and calcualte score
vec =c()

for (i in 1:length(first)){
  vec[i] <- split2(first[i], second[i], third[i])
}
num <- match(vec, c(letters,LETTERS))
sum(num)
