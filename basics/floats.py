float1 = 3.125              # standard notation
float2 = 3e8                # scientific notation  3 x 10^8 speed of light
float3 = 1.616e-35          # scientific notation  planck's constant very small numbers
float4 = float(7)
float5 = float("1.618")
float6 = float("nan")
float7 = float("inf")
float8 = float("-inf")
float9 = 3.0 + 1


def main():
    floatNumbers = [
        float1,
        float2,
        float3,
        float4,
        float5,
        float6,
        float7,
        float8,
        float9
    ]
    [print(x) for x in floatNumbers]


if __name__ == "__main__":
    main()
