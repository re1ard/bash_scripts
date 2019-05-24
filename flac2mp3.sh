#!/bin/bash
#Конвертируем flac в mp3 12 потоками черерз ffmpeg используя xargs
#convert flac's in mp3's use 12 threads use ffmpeg and xargs
find *.flac -print0 | xargs -0 -P 12 -n 1 -I % ffmpeg -i % -ab 320k ./mp3/%.mp3
