library(fields)
library(dplyr)
library(RColorBrewer)

pallette <- colorRampPalette(c("#9E0142", "#FFFFBF", "#5E4FA2"))(100)

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

make_png <- function (files, save_dir) {

    dir.create(paste("png/", save_dir, sep=""))
    print("making png")
    for (f in files) {
        if (grepl("\\.txt$", f, ignore.case = TRUE)) next
        dat <- as.matrix(read.csv(f, header = F)) %>% t
        cat(".")
        colors <- dat %>% sort %>% filter_data %>% sapply (get_color)
        name <- gsub(".*/([^/]+)\\..*", "\\1", f)
        png(paste("png/", save_dir, "/", name, ".png", sep=""), width = 512, height = 512)
        image.plot(dat, col=colors)
        dev.off()
    }
    cat("\n")
    print("done")
}


