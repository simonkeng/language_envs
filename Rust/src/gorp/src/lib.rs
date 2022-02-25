use std::error::Error;
use std::fs;

use colored::*;

pub struct Config {
    pub search_string: String,
    pub filename: String,
}

impl Config {
    pub fn new(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("2 arguments are required.")
        }

        let search_string = args[1].clone();
        let filename = args[2].clone();

        Ok(Config { search_string, filename })
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.filename)?;
    // println!("Contents: \n{}", contents.yellow());

    let results = search(&config.search_string, &contents);
    if results.len() < 2 {
        println!("\n{} {} {}", "Keyword".red(), &config.search_string.bold(), "not found".red())
    }
    for line in results {
        println!("{}", line.green());
    }

    Ok(())
}

pub fn search<'a>(search_string: &str, contents: &'a str) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(search_string) {
            results.push(line);
        }
    }
    results
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let term = "Error";
        let contents = "\
Traceback (most recent call last):
File /scr/ob_scheduler/git-utils/ob_scheduler.py, line 142, in <module>
main()
raise RuntimeError(Today isn't OB date)";

        assert_eq!(vec!["raise RuntimeError(Today isn't OB date)"], search(term, contents));
    }
}