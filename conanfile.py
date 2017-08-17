from conans import ConanFile


class ParsonConan(ConanFile):
    name = "Parson"
    version = "0.0.1"
    generators = "cmake" 
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/bincrafters/conan-parson"
    source_url = "https://github.com/kgabis/parson"
    description = "Lightweight JSON library written in C."
    
    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=50 {0}.git"
                     .format(source_url)) 

    def build(self):
        
        
    def package(self):
        self.copy(pattern="parson.h", dst="include", src="")		
        self.copy(pattern="*", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()

