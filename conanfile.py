#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake, tools


class ParsonConan(ConanFile):
    name = "parson"
    version = "0.1.0"
    homepage = "https://github.com/kgabis/parson"
    url = "https://github.com/bincrafters/conan-parson"
    description = "Lightweight JSON library written in C."
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"

    def source(self):
        tools.get("https://github.com/kgabis/parson/archive/master.zip")
        os.rename("parson-master", "parson")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src="parson", keep_path=False)
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
