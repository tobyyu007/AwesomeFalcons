knitr::opts_chunk$set(echo = TRUE)

library(ggplot2)
library(rmarkdown)
library(apsimx)

# Latitude Longitude
# Upper left: 38.637354392601544, -122.1413878499751
# Upper right: 38.639079445152404, -121.6179782095487
# Lower left: 38.24295968306687, -122.13917937047962
# Lower left: 38.241225138023374, -121.61687396980096
# Google maps: https://goo.gl/maps/ZNbXkDT3hYwZEjUm8


stringify_coord <- function(coord) {
  if (coord < 0) {
      # print("coord is negative")
      scoord <- paste("m", as.character(-1*coord), sep = "")
  } else {
      # print("coord is non-negative")
      scoord <- as.character(coord)
  }
  # print(paste("scoord is:", scoord, sep = ""))
  return(scoord)
}

# sdir is for source directory; tdir is for target directory
inject_soil_profile <- function(sdir, tdir, sector, lon, lat, model) {
  sp <- get_isric_soil_profile(lonlat = c(lon, lat))
  tag <- paste("-sector-", as.character(sector), sep="")
  edit_apsimx_replace_soil_profile(
    file = paste("_", model, ".apsimx", sep=""),
    src.dir = sdir,
    wrt.dir = tdir,
    soil.profile = sp,
    edit.tag = tag,
    overwrite = FALSE,
    verbose = TRUE
  )
}

data <- read.table("centroids.csv", sep = ",", header=1)
lll <- lapply(1:nrow(data), function(i) as.numeric(data[i,]))
print(lll)


sdir <- "./src"
tdir <- "./output"

models <- c("Maize", "Soybean", "Wheat");
for (lonlat in lll) {
  for (model in models) {
    inject_soil_profile(sdir, tdir, lonlat[1], lonlat[3], lonlat[2], model)
  }
}