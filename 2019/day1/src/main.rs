use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
	let mut total = 0;
	let mut total_rec = 0;

    if let Ok(lines) = read_lines("/home/rutger/Programming/AdventOfCode/2019/input/day1_1") {
        for line in lines {
            if let Ok(input) = line {
				let parsed = input.parse::<u32>();
				let nb = match parsed {
					Ok(x) => x,
					Err(_) => 0
				};

				total += calculate_fuel_consumption(nb);
				total_rec += calculate_fuel_consumption_rec(nb);
            }
        }
    }

	println!("Total {}", total);
	println!("Total rec {}", total_rec);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn calculate_fuel_consumption(x: u32) -> u32 {
	if x < 9 {
		return 0;
	}
	x / 3 - 2
}

fn calculate_fuel_consumption_rec(x: u32) -> u32 {
	if x < 9 {
		return 0
	}

	let c = calculate_fuel_consumption(x);
	c + calculate_fuel_consumption_rec(c)
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

    #[test]
    fn test_5() {
        assert_eq!(calculate_fuel_consumption_rec(1969), 966);
    }

    #[test]
    fn test_6() {
        assert_eq!(calculate_fuel_consumption_rec(100756), 50346);
    }
}
