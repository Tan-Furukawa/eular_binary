library(fields)
library(dplyr)

pallette <- colorRampPalette(c("white", "black"))(100)

create_color_gradient_maker <- function(pallette) {
    return (function (value) {
        index <- round(value * 100)
        index[index < 1] <- 1
        index[index > 100] <- 100
        color <- pallette[index]
            return(color)
    })
}

get_color <- pallette %>% create_color_gradient_maker

filter_data <- function (d) {
    d[d > 0.999] <- 0.999
    d[d < 0.001] <- 0.001
    return (d)
}

files <- list.files("../result/", pattern = "\\.csv")

for (f in files) {
    dat <- as.matrix(read.csv(paste("../result/",f, sep=""), header = F))
    colors <- dat %>% sort %>% filter_data %>% sapply (get_color)
    name <- gsub("\\..+$", "", f)
    png(paste("png/", name, ".png", sep=""), width = 512, height = 512)
    image.plot(dat, col=colors)
    dev.off()
}
