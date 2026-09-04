#include <algorithm>
#include <cstdint>
#include <iostream>
#include <queue>
#include <stdexcept>
#include <vector>

// Independent streaming check of the history-mask conjecture at n=9.
//
// This program does not reuse the Python Hurwitz-orbit generator.  It streams
// through all 9^7 Pruefer words, reconstructs the corresponding labelled tree,
// applies the rooted-tree inverse of the factorization--tree correspondence,
// and scans the first-collision scheduler.  Strict increase of execution
// indices means a single left-to-right scan records the complete history.
// The output is finite computational evidence, not an all-n proof.

struct Edge {
  int a;
  int b;
};

static Edge normalize(int a, int b) {
  if (a > b) {
    std::swap(a, b);
  }
  return {a, b};
}

static Edge conjugate(Edge edge, Edge by) {
  const auto swap_endpoint = [&](int x) {
    return x == by.a ? by.b : (x == by.b ? by.a : x);
  };
  return normalize(swap_endpoint(edge.a), swap_endpoint(edge.b));
}

int main() {
  constexpr int n = 9;
  constexpr int history_length = n - 2;
  constexpr unsigned mask_count = 1U << history_length;

  std::uint64_t total = 1;
  for (int i = 0; i < history_length; ++i) {
    total *= n;
  }

  std::vector<std::uint64_t> histories(mask_count, 0);
  std::vector<int> pruefer(history_length, 1);
  std::vector<int> degree(n + 1);
  std::vector<int> parent(n + 1);
  std::vector<int> cycle(n + 1);
  std::vector<int> relabel(n + 1);
  std::vector<std::vector<int>> adjacency(n + 1);
  std::vector<Edge> factorization(n - 1);

  for (std::uint64_t code = 0; code < total; ++code) {
    std::uint64_t remaining = code;
    for (int i = 0; i < history_length; ++i) {
      pruefer[i] = static_cast<int>(remaining % n) + 1;
      remaining /= n;
    }

    std::fill(degree.begin(), degree.end(), 1);
    for (int vertex : pruefer) {
      ++degree[vertex];
    }
    std::priority_queue<int, std::vector<int>, std::greater<int>> leaves;
    for (int vertex = 1; vertex <= n; ++vertex) {
      if (degree[vertex] == 1) {
        leaves.push(vertex);
      }
    }
    for (auto& neighbors : adjacency) {
      neighbors.clear();
    }
    for (int vertex : pruefer) {
      const int leaf = leaves.top();
      leaves.pop();
      adjacency[leaf].push_back(vertex);
      adjacency[vertex].push_back(leaf);
      if (--degree[vertex] == 1) {
        leaves.push(vertex);
      }
      --degree[leaf];
    }
    const int first = leaves.top();
    leaves.pop();
    const int second = leaves.top();
    leaves.pop();
    adjacency[first].push_back(second);
    adjacency[second].push_back(first);

    // Root the tree at n and form theta_i=(i,parent(i)), 1 <= i < n.
    std::fill(parent.begin(), parent.end(), 0);
    parent[n] = -1;
    std::vector<int> queue{n};
    for (std::size_t head = 0; head < queue.size(); ++head) {
      const int vertex = queue[head];
      for (int neighbor : adjacency[vertex]) {
        if (parent[neighbor] == 0) {
          parent[neighbor] = vertex;
          queue.push_back(neighbor);
        }
      }
    }

    // Compute C_R=theta_1 ... theta_{n-1}; rightmost factor acts first.
    for (int vertex = 1; vertex <= n; ++vertex) {
      cycle[vertex] = vertex;
    }
    for (int i = 1; i < n; ++i) {
      std::swap(cycle[i], cycle[parent[i]]);
    }

    // The unique relabelling mu sends n,C_R(n),...,C_R^{n-1}(n)
    // to 1,2,...,n.  Then tau_i=(mu(i),mu(parent(i))) factors c_n.
    int source = n;
    int target = 1;
    for (int k = 0; k < n; ++k) {
      relabel[source] = target;
      source = cycle[source];
      target = target % n + 1;
    }
    for (int i = 1; i < n; ++i) {
      factorization[i - 1] = normalize(relabel[i], relabel[parent[i]]);
    }

    unsigned mask = 0;
    for (int i = 0; i < history_length; ++i) {
      if (factorization[i].a == factorization[i + 1].a) {
        mask |= 1U << i;
        const Edge left = factorization[i];
        const Edge right = factorization[i + 1];
        factorization[i] = right;
        factorization[i + 1] = conjugate(left, right);
      }
    }
    ++histories[mask];
  }

  bool law_holds = true;
  std::cout << "first-collision Hurwitz independent n=9 stream\n";
  std::cout << "n=" << n << " pruefer_words=" << total
            << " masks=" << mask_count << '\n';
  for (unsigned mask = 0; mask < histories.size(); ++mask) {
    const int executions = __builtin_popcount(mask);
    std::uint64_t expected = 1;
    for (int i = 0; i < history_length - executions; ++i) {
      expected *= n - 1;
    }
    if (histories[mask] != expected) {
      law_holds = false;
    }
    std::cout << "mask=" << mask << " observed=" << histories[mask]
              << " expected=" << expected << '\n';
  }
  std::cout << "conjecture_status=n9_verified_not_claimed_all_n\n";
  std::cout << "status=" << (law_holds ? "PASS" : "FAIL") << '\n';
  return law_holds ? 0 : 1;
}
