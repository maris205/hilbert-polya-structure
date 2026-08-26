use strict;
use warnings;

my $two_column = '\\begin{longtable}[]{@{}ll@{}}';
my $wrapped_two_column = '\\begin{longtable}[]{@{}>{\\raggedright\\arraybackslash}p{0.28\\textwidth}>{\\raggedright\\arraybackslash}p{0.64\\textwidth}@{}}';

while (<>) {
    s/\Q$two_column\E/$wrapped_two_column/g;
    s/(?<![0-9a-f])([0-9a-f]{64})(?![0-9a-f])/'\\seqsplit{' . $1 . '}'/ge;
    print;
}
