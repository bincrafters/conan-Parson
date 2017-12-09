import os
from conans import ConanFile, CMake, tools


class ParsonConan(ConanFile):
    name = "Parson"
    version = "0.1.0"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    homepage = "https://github.com/kgabis/parson"
    url = "https://github.com/bincrafters/conan-parson"
    author = "Bincrafters <bincrafters@gmail.com>"
    source_url = "https://github.com/kgabis/parson"
    description = "Lightweight JSON library written in C."
    options = {"shared": [True, False]}
    default_options = "shared=False"
    license = "https://github.com/kgabis/parson/blob/master/LICENSE"
    exports_sources = ["LICENSE", "CMakeLists.txt"]

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
