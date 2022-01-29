use std::io;

fn main() {
    println!("Hello, world!");

    let mut guess = String::new();

    io::stdin().read_line(&mut guess)
        .expect("Invalid input value.");

    println!("Your guess is {}", guess);

}
