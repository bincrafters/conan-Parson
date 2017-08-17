project(Parson)
cmake_minimum_required(VERSION 2.8)

add_library(Parson
	parson.c
)

target_include_directories(Parson
	Public
		include
)