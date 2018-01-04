#include <iostream>
#include <fstream>
#include <string>
#include <stdexcept>
#include <cctype>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>

#include <cassert>

#include "ezOptionParser.hpp"

#include "MCNPInput.hpp"

#include "exporter.hpp"
#include "exportfluka.hpp"

void usage(ez::ezOptionParser& opt) {
	std::string use;
	opt.getUsage(use);
	std::cout << use;
}

int main(int argc, const char* argv[]){

  ez::ezOptionParser opt;

  opt.overview = "csg2csg: A tool to convert MC CSG geometry formats";
  opt.syntax = "csg2csg [OPTIONS] --input [...] --output [...]";
  opt.example = "csg2csg --input test.mcnp --output output.fluka";

  opt.add(
	  "", // Default.
	  0, // Required?
	  0, // Number of args expected.
	  0, // Delimiter if expecting multiple args.
	  "Display usage instructions.", // Help description.
	  "-h",     // Flag token. 
	  "-help",  // Flag token.
	  "--help" // Flag token.
	  );

  opt.add(
	  "input.txt", // Default.
	  0, // Required?
	  1, // Number of args expected.
	  0, // Delimiter if expecting multiple args.
	  "File to import arguments.", // Help description.
	  "-i",     // Flag token. 
	  "--import" // Flag token.
	  );

  opt.add(
	  "output.txt", // Default.
	  0, // Required?
	  1, // Number of args expected.
	  0, // Delimiter if expecting multiple args.
	  "File to Export arguments.", // Help description.
	  "-o",     // Flag token. 
	  "--export" // Flag token.
	  );
  
  opt.parse(argc, argv);

  if(opt.isSet("-h") || opt.isSet("--help")) {
    usage(opt);
    return 1;
  }

  std::string import;
  if(opt.isSet("-i")) {
    opt.get("-i")->getString(import);   
  } else {
    std::cout << "No input set" << std::endl;
    return 1;
  }
  
  std::string output;
  if(opt.isSet("-o")) {
    opt.get("-o")->getString(output);
  } else {
    std::cout << "No export set" << std::endl;
    return 1;
  }
  std::cout << "Reading input file..." << std::endl;
  std::ifstream input;
  input.open(import);
  InputDeck& deck =InputDeck::build(input);
  Exporter *exp = new ExporterFluka::ExporterFluka(deck,"output");
  delete exp;
  //exp->Export();
  std::cout << "Done reading input." << std::endl;
 
  return 0;

}
