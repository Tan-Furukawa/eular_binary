library(magick)
library(magrittr)


sort_files_by_number <- function(file_list) {
    numeric_part <- gsub("[^0-9]", "", file_list)
    numeric_part <- as.numeric(numeric_part)
    sorted_files <- file_list[order(numeric_part)]
    return(sorted_files)
}

list.files(path='png/', pattern = '*.png', full.names = T) %>% 
    sort_files_by_number %>%
    image_read() %>% # reads each path file
    image_join() %>% # joins image
    image_animate(fps=20) %>% # animates, can opt for number of loops
    image_write("FileName3.gif") # write to current dir