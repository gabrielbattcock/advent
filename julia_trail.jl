# Julia trial 

#= 

Multiple line 
=#
println("Hello world")

my_pi = 3.14159

my_pi^2

days = 2
println(typeof(days))
days = convert(Float64, days)
println(typeof(days))

vector = [1,2,3,4,5,6]
for i in vector
    println(i)
end

string = "hello world"

for i in string
    println(i)
end

function Babylonian(x; N=10)
    t = (1+x)/2
    for i = 2:N;t = (t+x/t)/2 end
    t
end

function highest(x,y)
    if x > y
        return x 
    if x < y
        return y
    else
        return
