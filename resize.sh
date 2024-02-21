#!/bin/bash

mkdir results

mogrify -path results -quality 10 -resize 1152x2048! *.jpg




