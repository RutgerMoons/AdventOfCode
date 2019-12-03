use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
	let input = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,1,23,6,27,1,6,27,31,1,13,31,35,1,13,35,39,1,39,13,43,2,43,9,47,2,6,47,51,1,51,9,55,1,55,9,59,1,59,6,63,1,9,63,67,2,67,10,71,2,71,13,75,1,10,75,79,2,10,79,83,1,83,6,87,2,87,10,91,1,91,6,95,1,95,13,99,1,99,13,103,2,103,9,107,2,107,10,111,1,5,111,115,2,115,9,119,1,5,119,123,1,123,9,127,1,127,2,131,1,5,131,0,99,2,0,14,0";
	let result = solve_program(&input);
	println!("{}", result);

}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn solve_program(input: &str) -> String {
	let mut values : Vec<i32> = input.split(",")
									   .map(|x| x.parse::<i32>())
									   .map(|x| x.unwrap())
									   .collect();
	
	let mut pointer = 0;
	while pointer < values.len() {
		let opcode = values[pointer as usize];
		if opcode == 99 {
			break;
		}

		let op1 = values[values[pointer + 1] as usize];
		let op2 = values[values[pointer + 2] as usize];
		let dest : usize = (values[pointer + 3] as usize);

		let intermediary = match opcode {
			1 => op1 + op2,
			2 => op1 * op2,
			_ => 0,
		};
		values[dest] = (intermediary);
		pointer += 4;
	}

	(values.into_iter())
					    .map(|x| x.to_string())
						.collect::<Vec<String>>()
						.join(",")
}

#[cfg(test)]
mod tests {
	use super::*;

    #[test]
    fn test_1() {
        assert_eq!(solve_program("1,0,0,0,99"), "2,0,0,0,99");
    }
    #[test]
    fn test_2() {
        assert_eq!(solve_program("2,3,0,3,99"), "2,3,0,6,99");
    }
    #[test]
    fn test_3() {
        assert_eq!(solve_program("2,4,4,5,99,0"), "2,4,4,5,99,9801");
    }
    #[test]
    fn test_4() {
        assert_eq!(solve_program("1,1,1,4,99,5,6,0,99"), "30,1,1,4,2,5,6,0,99");
    }
	
}
