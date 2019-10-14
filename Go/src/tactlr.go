package main

import (
  "fmt"
  "log"
  "os"
  "io/ioutil"
  "github.com/urfave/cli"
)

var app = cli.NewApp()

func info() {
  app.Name = "Terminal Art Controller"
  app.Usage = "A CLI for generating blocks of ascii art"
  app.Author = "Simon Keng"
  app.Version = "1.0.0"
}


func commands() {
  app.Commands = []cli.Command {
    {
      Name: "machine",
      Aliases: []string{"m"},
      Usage: "Display Simon's machine",
      Action: func(c *cli.Context) {
        data, err := ioutil.ReadFile("resources/machine.txt")
        if err != nil {
          fmt.Println("File reading error: machine", err)
          return
        }
        fmt.Println(string(data))
      },
    },
    {
      Name: "cat",
      Aliases: []string{"c"},
      Usage: "Display Simon's cat",
      Action: func(c *cli.Context) {
        data, err := ioutil.ReadFile("resources/cat.txt")
        if err != nil {
          fmt.Println("File reading error: cat", err)
          return
        }
        fmt.Println(string(data))
      },
    },
  }
}


func main() {
  info()
  commands()

  err := app.Run(os.Args)
  if err != nil {
    log.Fatal(err)
  }
}

