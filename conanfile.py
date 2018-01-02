#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake, tools


class ParsonConan(ConanFile):
    name = "Parson"
    version = "0.1.0"
    homepage = "https://github.com/kgabis/parson"
    url = "https://github.com/bincrafters/conan-parson"
    description = "Lightweight JSON library written in C."
    license = "MIT"
    exports = ["LICENSE.md"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = ["CMakeLists.txt"]
    options = {"shared": [True, False]}
    default_options = "shared=False"

    def source(self):
        tools.get("https://github.com/kgabis/parson/archive/master.zip")
        os.rename("parson-master", "parson")

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src="parson", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
