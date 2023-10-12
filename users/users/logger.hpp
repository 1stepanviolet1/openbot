#pragma once

#include <iostream>


static size_t LOGGER_COUNTER;

#define log(msg) std::cout << "LOGGER{" << ++LOGGER_COUNTER << "}: ";\
				 std::cout << msg << std::endl;
