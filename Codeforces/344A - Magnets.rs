use std::io;

fn main() {
    let mut magnet_count = String::new();
    io::stdin().read_line(&mut magnet_count).expect("ERR0");
    let lines: Vec<String> = io::stdin()
        .lines()
        .filter(|x| x.is_ok())
        .map(|x| x.unwrap())
        .collect();
    let mut groups = 0;
    let mut last_magnet = &lines[0];
    for i in 1..lines.len() {
        if &lines[i] != last_magnet {
            groups += 1;
            last_magnet = &lines[i];
        }
    }
    if groups == 0 {
        println!("1")
    } else {
        println!("{}", groups + 1);
    }
}