#!/usr/bin/env ruby
one = ARGV[0].scan(/\[from:(.*?)\]/).join
two = ARGV[0].scan(/\[to:(.*?)\]/).join
three = ARGV[0].scan(/\[flags:(.*?)\]/).join
puts "#{one},#{two},#{three}"
