use std::env;
use std::process;

use colored::*;

use gorp::Config;

fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::new(&args).unwrap_or_else(|err| {
        println!("Could not parse arguments: {}", err);
        process::exit(1);
    });

    println!("Searching for: {}", config.search_string.blue());
    println!("In file: {}", config.filename.purple());

    if let Err(e) = gorp::run(config) {
        println!("Program error: {}", e);
        process::exit(1);
    }

}

