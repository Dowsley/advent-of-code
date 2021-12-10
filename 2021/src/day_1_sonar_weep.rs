use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;

fn load_from_file(file_path: &str) -> Vec<i64> {
    let file = File::open(file_path).expect("file wasn't found.");
    let reader = BufReader::new(file);

    let numbers: Vec<i64> = reader
        .lines()
        .map(|line| line.unwrap().parse::<i64>().unwrap())
        .collect();
    return numbers;
}

fn solve_part_1(numbers: Vec<i64>) {
    let mut num_of_increases: i64 = 0;
    let mut prev_n: i64 = numbers[0];
    
    for (i, n) in numbers.iter().enumerate() {
        if i != 0 {
            if *n > prev_n {
                num_of_increases += 1;
                //println!("{}: Increased", *n);
            } else {
                //println!("{}: Decreased", *n);
            }
            prev_n = *n;
        } else {
            //println!("{}: No previous number", *n);
        }
    }

    println!("[[DAY 1 PART 1]] Number of increases: {}", num_of_increases);
}

fn solve_part_2(numbers: Vec<i64>) {
    let mut num_of_increases: i64 = 0;
    let vec_len = numbers.len();
    
    let mut prev_sum: i64 = 0;
    let mut sum: i64 = 0;
    for (i, _n) in numbers.iter().enumerate() {
        if vec_len-1 >= i+2 {
            if i == 0 {
                sum += numbers[i];
                sum += numbers[i+1];
                sum += numbers[i+2];
                sum += numbers[i+2];
                prev_sum = sum;
                //println!("{} + {} + {}: {} No previous window", numbers[i], numbers[i+1], numbers[i+2], sum);

            } else {
                sum -= numbers[i-1];
                sum += numbers[i+2];
                
                if sum > prev_sum {
                    num_of_increases += 1;
                    //println!("{} + {} + {}: {} Increased", numbers[i], numbers[i+1], numbers[i+2], sum);
                } else {
                    //println!("{} + {} + {}: {} Decreased", numbers[i], numbers[i+1], numbers[i+2], sum);
                }
                prev_sum = sum;
            }
        }
    }

    println!("[[DAY 1 PART 2]] Number of increases: {}", num_of_increases);
}

pub fn get_solution() {
    let numbers: Vec<i64> = load_from_file("input.txt");
    solve_part_1(numbers.clone());
    solve_part_2(numbers.clone());
}
