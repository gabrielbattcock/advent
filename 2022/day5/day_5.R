#day 5 of the advent

library(tidyverse)

setwd("Documents/programming_projects/advent")

data <- readLines("crane.txt") 

boxes <- data[1:9]
moves <- data[ 11:length(data)]


test_string <- moves[1]
boxes[1]

int_move <- function(move_line){
  a <- unlist(regmatches(move_line, gregexpr("[[:digit:]]+", move_line)))
  move <- as.integer(a[1])
  from <- as.integer(a[2])
  to <- as.integer(a[3])
  c(move,from, to)
}



