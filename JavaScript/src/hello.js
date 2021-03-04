
const chalk = require('chalk');
const boxen = require('boxen');

var log = console.log;

var hi = chalk.blue.bold('Hello ') + chalk.green.bold('World ') +
                chalk.red('!') + '\n';

log(boxen(hi, { padding: 3 }))