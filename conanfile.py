from conans import ConanFile, CMake, tools


class ParsonConan(ConanFile):
    name = "Parson"
    version = "0.0.1"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/bincrafters/conan-parson"
    source_url = "https://github.com/kgabis/parson"
    description = "Lightweight JSON library written in C."
    license = "https://opensource.org/licenses/mit-license.php"
    exports = ["LICENSE"]
    exports_sources = ["CMakeLists.txt"]
    release_name = name.lower()

    def source(self):
        self.run("git clone --depth=50 {0}.git".format(self.source_url))

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst=".", src=".")
        self.copy(pattern="parson.h", dst="include", src=self.release_name)
        self.copy(pattern="*.a", dst="lib", src=".")
        self.copy(pattern="*.so*", dst="lib", src=".")
        self.copy(pattern="*.dylib", dst="lib", src=".")

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()
