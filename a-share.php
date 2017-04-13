<?php

$buyPrice = 395.39;

if (!isset($argv[1])) {
    $share = 200;
} else {
    $share = $argv[1];
}

echo('buying price: '. getTotalPrice($buyPrice, $share).PHP_EOL);

function getTotalPrice($price, $share) {
    $taxRate = 0.001;
    $exchangeRate = 0.00004;
    $exchangeFee = 10;
    return $price * (1 + $taxRate + 2 * ($exchangeRate + $exchangeFee /($share * $price)));
    // return $price * (1 + 0.001 + 2 * (0.00004 + 10 /($share * $price)));
}