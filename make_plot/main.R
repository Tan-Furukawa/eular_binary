source("make_gif.R")
source("plot_png.R")
library("jsonlite")
library("future")

unlink("png", recursive = TRUE)
dir.create("png")

get_date <- function(string) {
    pattern <- "\\d{4}_\\d{2}_\\d{2}_\\d{2}_\\d{2}_\\d{2}"
    date <- regmatches(string, regexpr(pattern, string))
    return(date)
}

update_file_status <- function(name) {
    json_data <- fromJSON("../result//done.json")
    json_data[json_data$file == name,]$done <- TRUE
    jsonlite::write_json(json_data, path = "../result//done.json")
}

files <- list.files("../result/", full.names = TRUE)
non_json_files <- files[!grepl("\\.json$", files, ignore.case = TRUE)]
json <- files[grepl("\\.json$", files, ignore.case = TRUE)]

dir <- fromJSON(json)
target_files <- dir$file[!dir$done]

target_files %>% 
sapply(function(x) { # pickup the path of target file
    f <- non_json_files %>% sapply (function (y) {
        return (grepl(x, y))
    })
    return (non_json_files[f])
})%>% 
lapply (function (x) {
    list.files(x, full.names = TRUE)
})%>%
sapply(function (x) {
    make_png(x, get_date(x[1]))
})


list.files("png", full.names = TRUE) %>%
    sapply (function(f) {
        update_file_status(get_date(f))
        res <- future({make_gif(f, get_date(f))})
    })




