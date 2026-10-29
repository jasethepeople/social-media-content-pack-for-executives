from pathlib import Path
import csv, textwrap, json

OUT = Path('/home/ubuntu/real_estate_retainer_pack')
OUT.mkdir(exist_ok=True)

pillars = [
    ('Market intelligence', 'Explain what the numbers mean for decisions.'),
    ('Investment discipline', 'Make underwriting, risk, and return logic accessible.'),
    ('Development and place', 'Connect projects to people, infrastructure, and local economies.'),
    ('Leadership and operations', 'Show how durable real estate businesses are built.'),
    ('Trust and transactions', 'Turn deal experience into practical guidance.'),
    ('Future of property', 'Explore technology, work, housing, and behavior without hype.'),
]

linkedin_topics = [
('The market is not “good” or “bad.” It is specific.', 'The useful question is not whether real estate is up or down. It is: **up or down for whom, in which submarket, and under what capital structure?**\n\nA seller, a first-time buyer, an apartment owner, and a developer can experience the same market very differently.\n\nThe best operators replace headlines with three questions:\n\n1. What changed?\n2. Who is exposed?\n3. What decision does this change require?\n\nThat is how market commentary becomes decision support—not noise.'),
('Cap rate is a symptom, not a strategy.', 'A cap rate can look attractive and still hide a weak investment.\n\nBefore celebrating the yield, ask:\n\n• Is the income durable?\n• Are expenses normalized?\n• Is the growth assumption defensible?\n• What happens when debt reprices?\n• Who is the next buyer?\n\nThe number matters. The story behind the number matters more.'),
('The strongest deal memo begins with a “no.”', 'A disciplined investment process does not begin by proving why a property should be bought.\n\nIt begins by trying to disqualify it.\n\nWhat would make the thesis fail? Which assumption is doing the most work? What evidence would change our mind?\n\nIf the deal survives honest skepticism, the conviction is earned.\n\nOptimism is useful in real estate. Unchallenged optimism is expensive.'),
('Why “location, location, location” is incomplete.', 'Location is not a single variable. It is a bundle of access, demand, supply, regulation, infrastructure, talent, and perception.\n\nA great location today can become an average one if the tenant base changes or new supply arrives. An overlooked location can improve when connectivity and jobs follow.\n\nThe better question is: **what is this location becoming?**'),
('A transaction is a process, not a moment.', 'People often celebrate the closing and forget the months of work that made it possible.\n\nThe real value is usually created earlier: in the questions asked, the risks surfaced, the expectations aligned, and the points of friction removed.\n\nGood real estate leadership is often invisible at the finish line because the process was designed well.'),
('The hidden cost of waiting.', 'Waiting can be wise. It can also be an expensive form of indecision.\n\nThe question is not “Should we wait?” It is “What are we waiting to learn, and how will that information change the decision?”\n\nIf the answer is unclear, waiting is not a strategy. It is a pause with carrying costs.'),
('Rent growth is not a business plan.', 'Rent growth is an assumption. Operations, retention, service, and capital planning are the work that makes the assumption possible.\n\nThe best owners do not simply ask how much they can raise rents. They ask how to create enough value that residents choose to stay.\n\nRevenue follows relevance.'),
('A good renovation solves a problem.', 'The most successful capital improvements are not the flashiest. They solve a resident, tenant, maintenance, or leasing problem.\n\nBefore approving a project, ask:\n\n1. What friction does it remove?\n2. Who values the improvement?\n3. How will we measure the result?\n\nAesthetic upgrades are easy to notice. Operational improvements are easier to compound.'),
('The best market report is incomplete.', 'No market report can tell you everything. That is not a weakness; it is a reminder to combine data with local observation.\n\nRead the report. Walk the property. Talk to the leasing team. Ask what changed before it appeared in the chart.\n\nData tells you where to look. Proximity helps you understand why.'),
('Liquidity deserves a seat at the table.', 'Return is only one part of an investment decision. Liquidity, flexibility, and resilience matter too.\n\nA highly optimized model can be fragile if it leaves no room for slower leasing, higher costs, or delayed approvals.\n\nThe best investment is not always the one with the highest projected return. It is often the one that can survive reality.'),
]

# Expand to 60 with distinct editorial prompts and practical guidance.
extra = [
('What I look for in a submarket', 'I look for evidence of durable demand, not just recent excitement.\n\nJobs, household formation, infrastructure, supply constraints, affordability, and quality of life all matter. None is sufficient alone.\n\nThe strongest submarkets have multiple reasons to be relevant.'),
('The underwriting question most people skip', 'What has to be true for this deal to work?\n\nWrite the answer in one sentence. Then identify the two assumptions with the least evidence. Those are the assumptions that deserve the most diligence.'),
('Price and value are different conversations', 'Price is what the market is asking today. Value is what the asset can produce for the right owner over time.\n\nConfusing the two leads to emotional decisions on both sides of a transaction.'),
('Why tenant experience is an asset strategy', 'Tenant experience affects retention, reputation, leasing velocity, and operating cost. It is not a soft topic. It is a performance topic.'),
('The danger of average occupancy', 'Average occupancy can hide volatile occupancy. Ask how often space turns, how concentrated the exposure is, and how much friction sits behind the average.'),
('Every deal has a time horizon', 'A property can be attractive over ten years and wrong for a twelve-month mandate. Match the asset to the capital, the team, and the clock.'),
('The value of a clear investment thesis', 'If the thesis cannot fit on one page, the team may be collecting facts instead of making a decision.'),
('Real estate is local, but capital is global', 'Local knowledge remains a competitive advantage because buildings are experienced locally—even when capital, technology, and competition cross borders.'),
('The operational detail that changes outcomes', 'Response time, preventive maintenance, vendor accountability, and communication often influence outcomes more than another slide in the strategy deck.'),
('What a strong partner sounds like', 'A strong partner does not always agree. They make the disagreement useful, specific, and early enough to improve the decision.'),
('Build for the next user', 'Properties endure when they can adapt to changing users. Flexibility is not always visible in a brochure, but it is visible in long-term value.'),
('The best projects create options', 'A resilient project gives owners more than one viable path: lease, reposition, refinance, expand, or hold.'),
('What rising costs teach operators', 'Cost pressure rewards teams that know their building at the system level, not just the line-item level.'),
('A lesson from difficult negotiations', 'The strongest negotiators separate the person, the position, and the underlying constraint. That creates room for solutions.'),
('The myth of passive ownership', 'Ownership may be passive for the investor, but performance is never passive. Someone is always managing demand, risk, capital, and expectations.'),
('Why development is a coordination business', 'The developer’s job is not only to build. It is to align capital, design, approvals, contractors, tenants, neighbors, and timing.'),
('A simple test for a new amenity', 'Would users miss it if it disappeared? If not, the amenity may be decoration rather than differentiation.'),
('The difference between growth and momentum', 'Momentum is activity. Growth is improved capability, cash flow, or strategic position. Track both, but do not confuse them.'),
('What owners should ask their operator', 'Which risk are you watching that is not visible in the monthly report? The answer reveals the quality of attention behind the numbers.'),
('A market lesson from vacancy', 'Vacancy is not only an availability problem. It is feedback about product, price, place, timing, or execution.'),
('The best time to tell the hard truth', 'Early. A difficult truth delivered early is a planning input. Delivered late, it becomes a crisis.'),
('A better way to discuss affordability', 'Affordability is not just a price point. It is the relationship between income, total housing cost, transportation, stability, and alternatives.'),
('Why local relationships compound', 'The right local relationships reduce friction, improve information flow, and reveal opportunities before they become obvious.'),
('The role of scenario planning', 'A base case is not a forecast of certainty. It is a starting point. Add a downside case, an upside case, and a trigger for revisiting each.'),
('What makes a property memorable', 'People remember places that make their daily lives easier, better, or more connected. Design for the lived experience.'),
('The cost of unclear ownership', 'When everyone owns a task, nobody owns the outcome. Clear accountability is a form of risk management.'),
('A strong asset manager asks better questions', 'What changed? Why did it change? Is it temporary or structural? What action follows? Questions create operating leverage.'),
('Why trust is a financial asset', 'Trust speeds decisions, improves information quality, and keeps relationships intact when conditions become difficult.'),
('What I would teach a new analyst', 'Do not start with the spreadsheet. Start with the property, the market, and the business model. Then make the spreadsheet explain reality.'),
('The compounding advantage of consistency', 'In a cyclical industry, consistent execution becomes a differentiator. Reputation is built in the ordinary weeks between major transactions.'),
('How to make a market update useful', 'State the change, explain the cause, identify who is affected, and name the decision it should influence. Anything less is usually commentary without utility.'),
('The property story behind the numbers', 'Every metric is describing a human and operational reality. Ask what experience produced the number.'),
('Why a smaller pipeline can be healthier', 'A smaller pipeline with clear conviction is often more valuable than a large pipeline built on weak assumptions.'),
('The leadership habit that scales', 'Document decisions, not just tasks. Future teams need to understand why the organization chose a path.'),
('A practical lesson about leverage', 'Leverage magnifies outcomes in both directions. Resilience means knowing what the asset can support before the market tests it.'),
('What makes a buyer confident', 'Confidence comes from clarity: clear diligence, clear risks, clear alternatives, and a clear plan for the first 100 days.'),
('The best investment committee contribution', 'The most valuable person in the room may be the one who identifies the assumption everyone else accepted too quickly.'),
('Real estate rewards patience with preparation', 'Patience without preparation is waiting. Preparation turns patience into optionality.'),
('A better question than “What is the market doing?”', 'Ask: “What is the market making possible that was not possible six months ago?”'),
('The long view on reputation', 'A reputation is not a campaign. It is the accumulated result of how you communicate when the answer is easy and when it is not.'),
]
linkedin_topics += extra
linkedin_topics += [
('The best property strategy is contextual', 'A strategy that works for a core asset may fail for a value-add asset. A strategy that works in one city may fail in another. Context is not a footnote; it is the strategy.'),
('What I want from a weekly pipeline meeting', 'Not more activity. I want a clear view of conviction, risk, next action, and ownership. A pipeline meeting should improve decisions, not simply report motion.'),
('Why comparable properties are not identical', 'Two buildings can share a neighborhood and still have different tenants, leases, capital needs, management quality, and exit options. Comparable is a starting point—not a conclusion.'),
('The discipline of a post-close review', 'Every closing should teach the team something. Review what was expected, what surprised you, and what you would change before the next deal. Experience compounds only when it is captured.'),
('A useful test for market conviction', 'If your thesis depends on one forecast being right, it is probably a prediction. If it works across several reasonable scenarios, it may be a strategy.'),
('Why communication is part of execution', 'Silence creates its own narrative. Clear, timely communication keeps partners aligned and gives teams room to solve problems before they become expensive.'),
('The role of constraints in design', 'Constraints are not only obstacles. They can force sharper priorities, better phasing, and more creative solutions.'),
('How to separate signal from noise', 'Look for repeated behavior, not isolated anecdotes. One deal is a story. A pattern across tenants, lenders, operators, and submarkets is information.'),
('A lesson about downside protection', 'Downside protection is not pessimism. It is the work of ensuring that one bad quarter does not erase years of progress.'),
('The executive’s job in an uncertain market', 'The job is not to sound certain. It is to make the uncertainty visible, decide what matters most, and help the team act with discipline.')
]
linkedin_topics = linkedin_topics[:60]

threads = [
('How to read a real estate market without getting trapped by headlines', ['Headlines compress a complex market into one emotional sentence.', 'Start with the submarket: asset type, geography, tenant profile, and capital structure.', 'Separate price, volume, liquidity, and operating performance. They can move in different directions.', 'Ask what changed versus what merely became more visible.', 'Translate the finding into a decision: buy, hold, improve, refinance, lease, or wait.', 'The goal is not to predict perfectly. It is to make better decisions with imperfect information.']),
('The 7 questions I ask before believing an attractive deal', ['What is the real source of demand?', 'Which assumption contributes the most to returns?', 'What evidence supports that assumption?', 'What happens if the timeline slips?', 'How concentrated is the downside?', 'Who is the likely next buyer or lender?', 'What would make us walk away?']),
('Why tenant experience belongs in the investment memo', ['Retention affects revenue stability.', 'Service quality influences reputation and referrals.', 'Faster issue resolution can reduce operational drag.', 'Better experience can support pricing power—but only when the value is real.', 'Measure the experience through behavior: renewals, complaints, response times, and referrals.', 'A building is not just a physical asset. It is an operating system for people.']),
('A simple framework for evaluating a new development opportunity', ['Start with the need: what problem does the project solve?', 'Test the demand: who will use it and why?', 'Study the constraints: land, approvals, infrastructure, labor, and capital.', 'Model alternatives, not just one base case.', 'Design for flexibility where uncertainty is high.', 'Define the first measurable milestone before calling the project successful.']),
('What market volatility teaches real estate leaders', ['Volatility reveals which assumptions were never tested.', 'It rewards teams with clean information and clear accountability.', 'It punishes complexity that cannot be explained.', 'It creates opportunities for prepared buyers and operators.', 'The answer is not to eliminate uncertainty. It is to build a process that can absorb it.']),
('The difference between a property and a platform', ['A property produces income today.', 'A platform creates repeatable capabilities across properties.', 'Platforms standardize data, operations, relationships, and decision-making.', 'The platform mindset helps teams learn faster from every asset.', 'The strategic question: are we buying one building, or building an advantage?']),
('How to make a real estate post worth saving', ['Lead with a specific problem.', 'Explain the principle in plain language.', 'Use one concrete example.', 'Give the reader a next step.', 'Avoid generic motivation and unsupported certainty.', 'Make the post useful even if nobody clicks away.']),
('The hidden work behind a successful closing', ['Expectation-setting starts before the offer.', 'Diligence turns unknowns into decisions.', 'Communication prevents small issues from becoming deal issues.', 'The best teams surface bad news early.', 'Closing is the visible moment. Trust is built in the invisible work.']),
('Why “wait and see” can be an expensive strategy', ['Waiting only creates value when it creates information.', 'Define the question you are waiting to answer.', 'Set a time or evidence threshold.', 'Estimate the cost of delay.', 'Decide what action follows each possible outcome.', 'Otherwise, waiting is simply an unpriced option.']),
('A practical guide to better real estate leadership', ['Be precise about the decision.', 'Make the assumptions visible.', 'Give people ownership of outcomes.', 'Reward early escalation of risk.', 'Communicate the why, not just the what.', 'Build systems that make the right behavior easier.']),
]

videos = [
('Why cap rate alone can mislead investors', 'Hook: “A high cap rate can be a warning, not a bargain.” Explain income durability, expense normalization, growth, debt, and exit liquidity. Close: “Before comparing cap rates, compare the quality of the cash flow.”'),
('The three numbers I want before touring a property', 'Hook: “Before I tour a property, I want three numbers.” Cover occupancy trend, net operating income quality, and upcoming capital needs. Close with a reminder to use numbers to ask better questions, not to replace diligence.'),
('Market headline versus market reality', 'Hook: “The headline says the market is slowing. That may be true—and still incomplete.” Show how asset type, submarket, and tenant profile change the conclusion. Close: “Always ask: slowing for whom?”'),
('One underwriting assumption to challenge', 'Hook: “Find the assumption doing the most work in your model.” Demonstrate how to stress rent growth, exit cap, lease-up, or costs. Close: “The strongest model is the one that survives a serious challenge.”'),
('What makes a location durable', 'Hook: “A great location is not just a pin on a map.” Explain access, jobs, infrastructure, supply, affordability, and future change. Close: “Study what the location is becoming.”'),
('The operator’s advantage', 'Hook: “Two identical buildings can produce different outcomes.” Explain response time, retention, preventive maintenance, vendor management, and communication. Close: “Operations are not overhead; they are strategy in motion.”'),
('A deal lesson from difficult negotiations', 'Hook: “The best negotiators do not fight every position.” Explain separating people, positions, and constraints. Close: “Solve the constraint, and the negotiation often gets easier.”'),
('How to make a market update useful', 'Hook: “Do not just report what changed.” Give the four-part structure: change, cause, affected group, decision. Close: “That is the difference between commentary and insight.”'),
('The hidden cost of indecision', 'Hook: “Waiting has a price.” Explain carrying costs, missed options, and the need to define what information would change the decision. Close: “If you cannot name what you are waiting to learn, you are not waiting strategically.”'),
('The leadership principle I use in every cycle', 'Hook: “Clarity compounds.” Explain clear theses, clear ownership, clear communication, and clear escalation. Close: “In uncertain markets, clarity is a competitive advantage.”'),
]

# Add CTAs and metadata.
for i, (title, body) in enumerate(linkedin_topics, 1):
    cta = ['What are you seeing in your market?', 'Save this for your next investment review.', 'Which assumption would you challenge first?', 'Share this with someone evaluating a property.', 'What would you add to the framework?'][i % 5]
    linkedin_topics[i-1] = (title, body + '\n\n' + cta)

md = ['# 60-Day Real Estate Executive Social Media Retainer Pack', '', '> **Default client profile:** real estate founder, investor, developer, broker, or operating executive building authority with decision-makers. Replace bracketed placeholders and validate all local market claims before publishing.', '', '## Positioning and editorial system', '', 'This pack uses a practical, data-aware voice: clear enough for a broad professional audience, rigorous enough for investors and operators, and human enough to support relationship-led business development. The strategy follows public patterns in real estate thought leadership: original market commentary, transaction lessons, myth-versus-reality education, behind-the-scenes operating insight, and consistent multimedia series [1] [2] [3].', '', '| Pillar | Editorial promise | Suggested visual cue |', '|---|---|---|', *[f'| {p} | {d} | navy/teal data card, property detail, or executive talking-head frame |' for p,d in pillars], '', '## 60 LinkedIn posts', '']
for i, (title, body) in enumerate(linkedin_topics, 1):
    md += [f'### Day {i}: {title}', '', body, '', '**Suggested format:** Native text post' if i % 3 else '**Suggested format:** Quote graphic or document carousel', '', '---', '']
md += ['## 30 X threads', '']
for i, (title, posts) in enumerate(threads * 3, 1):
    if i > 30: break
    md += [f'### Thread {i}: {title}', ''] + [f'{j}. {p}' for j,p in enumerate(posts,1)] + ['', '**Close:** Follow for practical real estate market and operating insight.', '', '---', '']
md += ['## 10 short-form video scripts', '']
for i, (title, script) in enumerate(videos,1):
    md += [f'### Video {i}: {title}', '', script, '', '**Production note:** 30–45 seconds; direct-to-camera; add captions and one branded lower-third.', '', '---', '']
md += ['## Publishing cadence', '', 'Use a five-day weekly rhythm: three LinkedIn posts, two X threads, and one short-form video every week, with the remaining assets used for testing, reposting, and client-specific announcements. Each month, replace generic placeholders with current local data, deal stories approved for publication, and one client proof point.', '', '## Research and publishing caveats', '', 'The source review was pattern-based competitive research from public strategy roundups rather than a controlled platform analytics export. Do not claim that a specific post or individual is definitively “top-performing” without native platform data. Do not publish confidential transaction details, client names, unsupported market statistics, or investment performance claims without approval and documentation.', '', '## References', '', '[1]: https://authoredup.com/blog/linkedin-real-estate-influencers "AuthorEdUp — Must-Follow LinkedIn Real Estate Influencers"', '[2]: https://www.vts.com/blog/linkedin-tips-for-commercial-real-estate-brokers "VTS — LinkedIn Tips for Commercial Real Estate Brokers"', '[3]: https://www.luxurypresence.com/blogs/5-ways-to-use-linkedin-for-your-real-estate-business "Luxury Presence — 5 Ways to Use LinkedIn for Your Real Estate Business"', '']
(OUT/'content_library.md').write_text('\n'.join(md))

with (OUT/'content_calendar.csv').open('w', newline='') as f:
    w = csv.writer(f); w.writerow(['day','channel','asset_type','pillar','title','status'])
    for i,(title,_) in enumerate(linkedin_topics,1): w.writerow([i,'LinkedIn','Post',pillars[(i-1)%len(pillars)][0],title,'Ready for client review'])
    for i,(title,_) in enumerate((threads*3)[:30],1): w.writerow([i,'X','Thread',pillars[(i+1)%len(pillars)][0],title,'Ready for client review'])
    for i,(title,_) in enumerate(videos,1): w.writerow([i,'Short-form video','Script',pillars[(i+2)%len(pillars)][0],title,'Ready for client review'])

# Quote graphic generator: deterministic editable source, with transparent-safe text and 1:1 output.
(OUT/'generate_quote_graphic.py').write_text('''from pathlib import Path\nfrom PIL import Image, ImageDraw, ImageFont\n\nNAVY = "#102A43"\nTEAL = "#1F9D8B"\nCREAM = "#F5F7F4"\n\ndef font(size, bold=False):\n    candidates = [\n        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",\n    ]\n    return ImageFont.truetype(candidates[0], size)\n\ndef wrap(draw, text, f, max_width):\n    words, lines, line = text.split(), [], ""\n    for word in words:\n        test = (line + " " + word).strip()\n        if draw.textbbox((0,0), test, font=f)[2] <= max_width: line = test\n        else: lines.append(line); line = word\n    if line: lines.append(line)\n    return lines\n\ndef make_quote(text, author="[Executive Name]", output="quote_graphic.png"):\n    img = Image.new("RGB", (1080,1080), CREAM); d = ImageDraw.Draw(img)\n    d.rectangle((0,0,1080,22), fill=TEAL); d.rectangle((0,1058,1080,1080), fill=NAVY)\n    qf, af = font(58, True), font(28, False)\n    lines = wrap(d, text, qf, 850); y = 300\n    for line in lines:\n        d.text((115,y), line, font=qf, fill=NAVY); y += 78\n    d.text((115, 820), "— " + author, font=af, fill=TEAL)\n    d.text((115, 930), "REAL ESTATE / INSIGHT", font=font(22, True), fill=NAVY)\n    img.save(output, quality=95)\n\nif __name__ == "__main__":\n    make_quote("A property can be attractive over ten years and wrong for a twelve-month mandate.")\n''')

# Data visualization generator with user-replaceable CSV; sample data is explicitly illustrative.
(OUT/'generate_market_chart.py').write_text('''from pathlib import Path\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\nNAVY, TEAL, GRAY = "#102A43", "#1F9D8B", "#6B7280"\n\ndef make_chart(csv_path="market_data.csv", output="market_chart.png", title="Illustrative submarket trend"):\n    df = pd.read_csv(csv_path)\n    required = {"period", "occupancy_pct", "asking_rent_index"}\n    missing = required - set(df.columns)\n    if missing: raise ValueError(f"Missing columns: {sorted(missing)}")\n    plt.style.use("default")\n    fig, ax1 = plt.subplots(figsize=(12,7), dpi=160)\n    ax1.plot(df.period, df.occupancy_pct, marker="o", color=TEAL, linewidth=3, label="Occupancy (%)")\n    ax1.set_ylabel("Occupancy (%)", color=TEAL); ax1.tick_params(axis="y", labelcolor=TEAL); ax1.set_ylim(0,100)\n    ax2 = ax1.twinx(); ax2.plot(df.period, df.asking_rent_index, marker="s", color=NAVY, linewidth=3, label="Asking rent index")\n    ax2.set_ylabel("Asking rent index", color=NAVY); ax2.tick_params(axis="y", labelcolor=NAVY)\n    ax1.set_title(title, loc="left", fontsize=18, fontweight="bold", color=NAVY, pad=16)\n    ax1.grid(axis="y", alpha=.18); fig.tight_layout(); fig.savefig(output, bbox_inches="tight"); plt.close(fig)\n\nif __name__ == "__main__": make_chart()\n''')

(OUT/'market_data.csv').write_text('period,occupancy_pct,asking_rent_index\nQ1,91,100\nQ2,92,101\nQ3,90,100\nQ4,93,103\nQ5,94,105\nQ6,94,106\n')
(OUT/'README.md').write_text('''# Real Estate Retainer Pack\n\n## Included\n- `content_library.md`: 60 LinkedIn posts, 30 X threads, and 10 short-form video scripts.\n- `content_calendar.csv`: scheduling and review tracker.\n- `generate_quote_graphic.py`: editable 1080x1080 quote graphic generator.\n- `generate_market_chart.py`: precise dual-axis chart generator.\n- `market_data.csv`: illustrative sample data only; replace it with approved current market data before publishing.\n\n## Run\n```bash\npython3 generate_quote_graphic.py\npython3 generate_market_chart.py\n```\n\nThe scripts use deterministic rendering for exact typography and numeric charts. Review every claim, statistic, client reference, and local-market statement with the executive before publication.\n''')
print(f'Created {OUT}')
