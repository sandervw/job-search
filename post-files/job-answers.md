# If you had a long-running dbt model dependent on a large data source like clickstream events, what are some things you might do to speed it up?

First I'd profile it to find the actual bottleneck rather than guess. The biggest lever is usually making it incremental, with a merge or insert_overwrite strategy + a lookback window. Then I'd push filtering and column pruning as far upstream as possible, pre-aggregate the clickstream to the needed grain in a staging model, and materialize heavy intermediates as tables.

# A stakeholder asks you to build a 'monthly active customers' metric, but Finance and Product each have a different definition of 'active.' How do you handle this?

I'd get both definitions written down and, more importantly, ask for the purpose of each. Usually the right answer is two clearly named, separately documented metrics. I'd bring the owners together to agree on naming, grain, and source of truth, then govern each metric in the semantic layer with its logic, owner, refresh cadence, and known limitations documented.
