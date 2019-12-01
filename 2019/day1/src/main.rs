use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
	let mut total = 0;

    if let Ok(lines) = read_lines("/home/rutger/Programming/AdventOfCode/2019/input/day1_1") {
        for line in lines {
            if let Ok(input) = line {
				let parsed = input.parse::<u32>();
				let nb = match parsed {
					Ok(x) => calculate_fuel_consumption(x),
					Err(_) => 0
				};
				total += nb;
            }
        }
    }

	println!("{}", total);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn calculate_fuel_consumption(x: u32) -> u32 {
	x / 3 - 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_div() {
        assert_eq!(calculate_fuel_consumption(12), 2);
    }

    #[test]
    fn test_rem() {
        assert_eq!(calculate_fuel_consumption(14), 2);
    }

    #[test]
    fn test_3() {
        assert_eq!(calculate_fuel_consumption(1969), 654);
    }

    #[test]
    fn test_4() {
        assert_eq!(calculate_fuel_consumption(100756), 33583);
    }
}
