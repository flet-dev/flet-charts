import 'package:collection/collection.dart';
import 'package:equatable/equatable.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:flutter/material.dart';

import 'package:flet/flet.dart';
import 'utils/charts.dart';
import 'utils/scatter_chart.dart';

class ScatterChartControl extends StatefulWidget {
  final Control control;

  ScatterChartControl({Key? key, required this.control})
      : super(key: ValueKey("control_${control.id}"));

  @override
  State<ScatterChartControl> createState() => _ScatterChartControlState();
}

class _ScatterChartControlState extends State<ScatterChartControl> {
  @override
  Widget build(BuildContext context) {
    var animation = widget.control.getAnimation(
        "animation",
        ImplicitAnimationDetails(
            duration: const Duration(milliseconds: 150),
            curve: Curves.linear))!;
    var border = widget.control.getBorder("border", Theme.of(context));

    var leftTitles = parseAxisTitles(widget.control.child("left_axis"));
    var topTitles = parseAxisTitles(widget.control.child("top_axis"));
    var rightTitles = parseAxisTitles(widget.control.child("right_axis"));
    var bottomTitles = parseAxisTitles(widget.control.child("bottom_axis"));

    var interactive = widget.control.getBool("interactive", true)!;

    // Build list of ScatterSpotData
    final spots = widget.control.children('spots').map((spot) {
      var x = spot.getDouble('x', 0)!;
      var y = spot.getDouble('y', 0)!;
      return ScatterSpot(x, y,
          show: spot.getBool('visible', true)!,
          renderPriority: spot.getInt('render_priority', 0)!,
          xError: spot.get('x_error'),
          yError: spot.get('y_error'),
          dotPainter: spot.get("point") != null
              ? parseChartDotPainter(
                  spot.get("point"), Theme.of(context), null, null, 0)
              : FlDotCirclePainter(
                  radius: spot.getDouble("radius"),
                  color: spot.getColor("color", context) ??
                      Colors.primaries[
                          ((x * y) % Colors.primaries.length).toInt()],
                ));
    }).toList();

    final chart = ScatterChart(
      ScatterChartData(
        scatterSpots: spots,
        backgroundColor: widget.control.getColor("bgcolor", context),
        minX: widget.control.getDouble("min_x"),
        maxX: widget.control.getDouble("max_x"),
        minY: widget.control.getDouble("min_y"),
        maxY: widget.control.getDouble("max_y"),
        baselineX: widget.control.getDouble("baseline_x"),
        baselineY: widget.control.getDouble("baseline_y"),
        titlesData: FlTitlesData(
          show: (leftTitles.sideTitles.showTitles ||
              topTitles.sideTitles.showTitles ||
              rightTitles.sideTitles.showTitles ||
              bottomTitles.sideTitles.showTitles),
          leftTitles: leftTitles,
          topTitles: topTitles,
          rightTitles: rightTitles,
          bottomTitles: bottomTitles,
        ),
        borderData: FlBorderData(show: border != null, border: border),
        gridData: parseChartGridData("horizontal_grid_lines",
            "vertical_grid_lines", Theme.of(context), widget.control),
        scatterTouchData: ScatterTouchData(
            enabled: interactive,
            touchCallback: widget.control.getBool("on_event", false)!
                ? (evt, resp) {
                    var eventData =
                        ScatterChartEventData.fromDetails(evt, resp);
                    widget.control.triggerEvent("event", eventData.toMap());
                  }
                : null,
            longPressDuration:
                widget.control.getDuration("long_press_duration"),
            handleBuiltInTouches:
                widget.control.getBool("handle_built_in_touches", true)!,
            touchTooltipData:
                parseScatterTouchTooltipData(context, widget.control, spots)),
        scatterLabelSettings: ScatterLabelSettings(
          showLabel: true,
          getLabelFunction: (spotIndex, spot) {
            var dp = widget.control.children("spots")[spotIndex];
            return dp.getString("label_text", "")!;
          },
          getLabelTextStyleFunction: (spotIndex, spot) {
            var dp = widget.control.children("spots")[spotIndex];
            var labelStyle = dp.getTextStyle(
                "label_style", Theme.of(context), const TextStyle())!;
            if (labelStyle.color == null) {
              labelStyle =
                  labelStyle.copyWith(color: spot.dotPainter.mainColor);
            }
            return labelStyle;
          },
        ),
        showingTooltipIndicators: widget.control
            .children('spots')
            .asMap()
            .entries
            .where((e) => e.value.getBool("selected", false)!)
            .map((e) => e.key)
            .toList(),
        rotationQuarterTurns:
            widget.control.getInt('rotation_quarter_turns', 0)!,
        //errorIndicatorData: widget.control.get('error_indicator_data'),
      ),
      duration: animation.duration,
      curve: animation.curve,
    );

    return ConstrainedControl(
        control: widget.control,
        child: LayoutBuilder(
            builder: (BuildContext context, BoxConstraints constraints) {
          return (constraints.maxHeight == double.infinity)
              ? ConstrainedBox(
                  constraints: const BoxConstraints(maxHeight: 300),
                  child: chart,
                )
              : chart;
        }));
  }
}
