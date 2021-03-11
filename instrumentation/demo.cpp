#include <iostream>
#include <string>
#include <map>
#include <cstdint>

// Place trade structure test
struct Trade {
    uint64_t time;
    uint32_t security_id;
    uint8_t side;
    uint64_t price;
    uint32_t quantity;
} __attribute__((packed));

// Exchange rate structure test
struct BankExchange {
    std::string name;
    std::string exchange;
    double rate;
};

// Example definitions
void PlaceBuyTrade(Trade* trade) {}
void PlaceSellTrade(Trade* trade) {}

// Sample to demonstrate callback
int MarketLoop(void) {
    while (true) { /* ... */ }
    return 1;
}

// Entry point
int main(int argc, char** argv)
{
    MarketLoop(); // Sees when MarketLoop gets called using PinTool
    return 0;
}