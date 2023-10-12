#pragma once

#include <iostream>


static size_t LOGGER_COUNT;

#define log(msg) std::cout << "LOGGER{" << ++LOGGER_COUNT << "}: "; \
				 std::cout << msg << std::endl;
