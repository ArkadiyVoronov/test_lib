#ifndef STATEREPORTERLIB_STATEMESSAGE_H
#define STATEREPORTERLIB_STATEMESSAGE_H

#include <string>
#include <chrono>

#include "State.h"

namespace state_reporter {
    struct StateMessage {
        State state;
        std::string application;
        std::string module;
        std::string function;
        std::string description;
        std::chrono::steady_clock::time_point timestamp;

        StateMessage() = default;

        StateMessage(const std::chrono::steady_clock::time_point &timestamp, State state,
                     const std::string &module, const std::string &application, const std::string &function,
                     const std::string &description) :
                state(state), application(application), module(module), function(function), description(description),
                timestamp(timestamp) {

            if (module.empty()) {
                throw std::invalid_argument("module must not be empty");
            }

            if (application.empty()) {
                throw std::invalid_argument("application must not be empty");
            }
        }
    };
}
#endif //STATEREPORTERLIB_STATEMESSAGE_H
